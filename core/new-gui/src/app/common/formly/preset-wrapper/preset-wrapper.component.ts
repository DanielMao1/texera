import { Component, OnInit } from '@angular/core';
import { FieldWrapper } from '@ngx-formly/core';
import { cloneDeep, isEqual } from 'lodash';
import { Preset, PresetService } from 'src/app/workspace/service/preset/preset.service';
import { asType } from '../../util/assert';

export interface PresetKey {
  presetType: string;
  saveTarget: string;
  applyTarget: string;
}

@Component({
templateUrl: './preset-wrapper.component.html',
styleUrls: ['./preset-wrapper.component.scss'],
})
export class PresetWrapperComponent extends FieldWrapper implements OnInit {

  public searchResults: Preset[] = [];
  public fieldKey: string = '';
  private searchTerm: string = '';
  private presetType: string = '';
  private saveTarget: string = '';
  private applyTarget: string = '';
  private showAllResults = true;

  constructor( private presetService: PresetService ) { super(); }

  ngOnInit(): void {
    if (
      this.field.key === undefined ||
      this.field.templateOptions === undefined ||
      this.field.templateOptions.presetKey === undefined) {

      throw Error(`form preset-wrapper field ${this.field} doesn't contain necessary .key and .templateOptions.presetKey attributes`);
    }
    const presetKey = <PresetKey> this.field.templateOptions.presetKey;

    this.fieldKey = asType(this.field.key,'string');
    this.searchTerm = this.formControl.value !== null ? this.formControl.value : '';
    this.presetType = presetKey.presetType;
    this.saveTarget =  presetKey.saveTarget;
    this.applyTarget = presetKey.applyTarget;
    this.setSearchResults(this.presetService.getPresets(this.presetType, this.saveTarget), this.searchTerm);

    this.handleSavePresets();
    this.handleFieldValueChanges();
  }

  public applyPreset(preset: Preset) {
    this.presetService.applyPreset(this.presetType, this.applyTarget, preset);
  }

  public handleDropdownVisibilityEvent(visible: boolean) {
    console.log("handle drop", visible);
    if (visible) {
      this.showAllResults = true;
      this.setSearchResults(this.presetService.getPresets(this.presetType, this.saveTarget), this.searchTerm);
    }
  }

  public getEntryTitle(preset: Preset): string {
    return preset[this.fieldKey].toString();
  }

  public getEntryDescription(preset: Preset): string {
    return Object.keys(preset).filter(key => key !== this.fieldKey).map(key => preset[key]).join(', ');
  }

  public deletePreset(preset: Preset) {
    const presets = cloneDeep(this.presetService.getPresets(this.presetType, this.saveTarget))
      .filter(oldPreset => !isEqual(oldPreset, preset));

    this.presetService.savePresets(this.presetType, this.saveTarget, presets, `Deleted preset: ${this.getEntryTitle(preset)}`, 'error');
  }

  public setSearchResults(presets: Readonly<Preset[]>, searchTerm: string) {
    if (this.showAllResults) {
      this.searchResults = presets.slice();
    } else {
      this.searchResults = presets.filter(
        preset => preset[this.fieldKey].toString().replace(/^\s+|\s+$/g, '').toLowerCase().startsWith(searchTerm.toLowerCase())
      );
    }
  }

  private handleSavePresets() {
    this.presetService.savePresetsStream
      .filter((presets) => presets.type === this.presetType && presets.target === this.saveTarget)
      .subscribe({
        next: (saveEvent) => {
          this.setSearchResults(saveEvent.presets, this.searchTerm);
        }
      });
  }

  private handleFieldValueChanges() {
    this.formControl.valueChanges.subscribe({
      next: (value: string | number | boolean ) => {
        this.searchTerm = value.toString();
        this.showAllResults = false;
        this.setSearchResults(this.presetService.getPresets(this.presetType, this.saveTarget), this.searchTerm);
      }
    });
  }

}
